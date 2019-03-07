from tethys_sdk.base import TethysAppBase, url_map_maker


class EmilyDesign(TethysAppBase):
    """
    Tethys app class for Emily Design.
    """

    name = 'Emily Design'
    index = 'emily_design:home'
    icon = 'emily_design/images/icon.gif'
    package = 'emily_design'
    root_url = 'emily-design'
    color = '#0e5401'
    description = 'Shows mockups and proposal for final project.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='home',
                controller='emily_design.controllers.home'
            ),

            UrlMap(
                name='mockup',
                url='mockup',
                controller='emily_design.controllers.mockup'
            ),

            UrlMap(
                name='proposal',
                url='proposal',
                controller='emily_design.controllers.proposal'
            ),
        )
        return url_maps
