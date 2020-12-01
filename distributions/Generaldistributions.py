"""
Class for a general distribution with parameters
"""
class Distribution:

    def __init__(self, mu=0, sigma=1):
        self.mu = mu
        self.sigma = sigma
        self.data = []

    def read_data_file(self, file_name):
        """
        description: function to read in a file from a txt file
        :param file_name:
        :return: data list
        """
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line=file.readline()
            file.close()

            self.data = data_list

            

