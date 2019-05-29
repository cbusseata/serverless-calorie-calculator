class Activity:
    NAME = None
    """str: Activity name
    """

    def get_name(self):
        """Gets the activity name
        
        Returns:
            str: Name of the activity
        """
        return self.NAME

class Run(Activity):
    NAME = 'run'

class Walk(Activity):
    NAME = 'walk'
