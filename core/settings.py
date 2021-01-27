#   target = selected target from a list of pre-determined services [reddit, youtube]
#   mode = search || url [list]
#   include = (posts = True || False) what data will be extracted 
#   should also include tags and return a list of tags based on element to be extracted
#   example search_bar = "q", in scav: driver.find_element_by_name("q") or return[index]

class Profile():
    def __init__(self, mode, int_preset):
        self.mode = mode
        self.int_preset = int_preset

    def presetLoader(self):
        try:
            filename = "PRESET_" + self.int_preset + ".cfg"
            conf = open("core/presets/" + filename, "r")
            orders = conf.readlines()
            conf.close()
            return orders
        
        except OSError as error_msg:
            print("Error: Couldn't find 'PRESET' file at path.\nRun 'root/scripts/setup.py' to generate a new file or download a new one.[insert link]\n{}".format(error_msg))
            return None