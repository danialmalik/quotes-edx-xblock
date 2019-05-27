"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Integer, Scope, String
from xblock.fragment import Fragment


class QuotesXBlock(XBlock):
    """
    XBlock where students can save thier quotes or motivation one liners.
    """

    quote = String(help= 'Quote to be saved', default='', scope=Scope.user_state)
    has_score = False
    icon_class = 'other'

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the QuotesXBlock, shown to students
        when viewing courses.
        """
        html = self.resource_string("static/html/quotes.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/quotes.css"))
        frag.add_javascript(self.resource_string("static/js/src/quotes.js"))
        frag.initialize_js('QuotesXBlock')
        return frag


    @XBlock.json_handler
    def save_quote(self, data, suffix=''):
        """
        Save the quote for the user.
        """
        self.quote = data['quote'] or ''
        return {'quote': self.quote}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("QuotesXBlock",
             """<quotes/>
             """),
            ("Multiple QuotesXBlock",
             """<vertical_demo>
                <quotes/>
                <quotes/>
                <quotes/>
                </vertical_demo>
             """),
        ]
