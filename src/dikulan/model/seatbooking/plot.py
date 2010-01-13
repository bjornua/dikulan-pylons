import logging, PIL.Image as Image
from cStringIO import StringIO
log = logging.getLogger(__name__)


class Plot:
    def __init__(self, plot_list, background, resources):
        self.plot_list = plot_list
        self.background = background
        self.resources = resources
        
    def get_image(self):
        rlist = dict()
        for k,v in self.resources.iteritems():
            i = Image.open(v)
            compensate_center = i.size[0]//2, i.size[1]//2
            rlist[k] = i,compensate_center
        
        background = rlist[self.background][0]
        
        for coord,k in self.plot_list:
            r,compensate_center = rlist[k]
            # Center image
            coord = coord[0] - compensate_center[0], coord[1] - compensate_center[1]
            background.paste(r, coord, r)
        
        buffer = StringIO()
        background.save(buffer, 'png')
        return buffer.getvalue()
        
        
