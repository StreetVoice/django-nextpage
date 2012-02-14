from django import template
from django.http import Http404
from django.conf import settings

register = template.Library()

DEFAULT_PAGINATION = getattr(settings, 'PAGINATION_DEFAULT_PAGINATION', 20)
INVALID_PAGE_RAISES_404 = getattr(settings,
    'PAGINATION_INVALID_PAGE_RAISES_404', False)

def do_autopaginate(parser, token):
    """
    Splits the arguments to the autopaginate tag and formats them correctly.
    """
    split = token.split_contents()
    as_index = None
    context_var = None
    for i, bit in enumerate(split):
        if bit == 'as':
            as_index = i
            break
    if as_index is not None:
        try:
            context_var = split[as_index + 1]
        except IndexError:
            raise template.TemplateSyntaxError("Context variable assignment " +
                "must take the form of {%% %r object.example_set.all ... as " +
                "context_var_name %%}" % split[0])
        del split[as_index:as_index + 2]
    if len(split) == 2:
        return AutoPaginateNode(split[1])
    elif len(split) == 3:
        return AutoPaginateNode(split[1], paginate_by=split[2], 
            context_var=context_var)
    elif len(split) == 4:
        try:
            orphans = int(split[3])
        except ValueError:
            raise template.TemplateSyntaxError(u'Got %s, but expected integer.'
                % split[3])
        return AutoPaginateNode(split[1], paginate_by=split[2], orphans=orphans,
            context_var=context_var)
    else:
        raise template.TemplateSyntaxError('%r tag takes one required ' +
            'argument and one optional argument' % split[0])

class AutoPaginateNode(template.Node):
    def __init__(self, queryset_var, paginate_by=DEFAULT_PAGINATION, context_var=None):
        self.queryset_var = template.Variable(queryset_var)
        if isinstance(paginate_by, int):
            self.paginate_by = paginate_by
        else:
            self.paginate_by = template.Variable(paginate_by)
        self.context_var = context_var

    def render(self, context):
        if isinstance(self.paginate_by, int):
            paginate_by = self.paginate_by
        else:
            paginate_by = self.paginate_by.resolve(context)

        try:
            page = int(context['request'].GET.get('page', 1))
            page = 1 if page < 1 else page
        except ValueError:
            page = 1

        limit = paginate_by + 1

        offset = 0 if page == 1 else (page - 1) * limit - (page - 1)
        items = context[self.queryset_var.var]
        items = items[offset:limit + offset]

        items_count = len(list(items))

        #
        if items_count == 0 and page > 1:
            if INVALID_PAGE_RAISES_404:
                raise Http404('Invalid page requested.  If DEBUG were set to ' +
                    'False, an HTTP 404 page would have been shown instead.')

        context[self.queryset_var.var] = items[:limit - 1]

        context['page'] = page
        context['next_page'] = page + 1 if items_count == limit else None
        context['prev_page'] = page - 1 if page > 1 else None
        return u''


def paginate(context, hashtag=''):
    to_return = {
        'next_page': context['next_page'],
        'prev_page': context['prev_page'],
        'page': context['page'],
    }

    if 'request' in context:
        getvars = context['request'].GET.copy()
        if 'page' in getvars:
            del getvars['page']
        if len(getvars.keys()) > 0:
            to_return['getvars'] = "&%s" % getvars.urlencode()
        else:
            to_return['getvars'] = ''
    return to_return
    

register.inclusion_tag('nextpage/pagination.html', takes_context=True)(
    paginate)
register.tag('autopaginate', do_autopaginate)
