class Student: 
    def __init__(self, name, section, spanish, english, social_studies, science):
        self.name = name 
        self.section = section 
        self.spanish = float(spanish)
        self. english = float(english)
        self.social_studies = float(social_studies)
        self.science = float(science)

    def average(self): 
        return round((self.spanish + self.english + self.social_studies + self.science) / 4, 2)
    def to_dict(self): 
        return {
            "name": self.name,
            "section": self.section,
            "spanish": self.spanish,
            "english": self.english,
            "social_studies": self.social_studies,
            "science": self.science
        }