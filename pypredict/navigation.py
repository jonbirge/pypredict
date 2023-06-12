
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT
from pkg_resources import resource_filename

class Toolbar(NavigationToolbar2QT):

    def __init__(self, canvas, applicationWindow):
        img_path = resource_filename("pypredict","img/")
        self.toolitems = (
            ('Home', 'Reset original view', '{}home'.format(img_path), 'home'),
            ('Back', 'Back to previous view', '{}back'.format(img_path), 'back'),
            ('Forward', 'Forward to next view', '{}forward'.format(img_path), 'forward'),
            (None, None, None, None),
            # ('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
            ('Pan', 'Pan axes with left mouse, zoom with right', '{}move'.format(img_path), 'pan'),
            ('Zoom', 'Zoom to rectangle', '{}zoom'.format(img_path), 'zoom'),
            (None, None, None, None),
            # ('Save', 'Save the figure', 'filesave', 'save_figure'),
        )
        super(Toolbar, self).__init__(canvas, applicationWindow)
