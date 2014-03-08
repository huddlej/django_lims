from django.db import models
import ncbi


class Clone(models.Model):
    """
    Represents DNA for a clone identified by a unique name and living in a
    cellular environment like a bacterium or yeast.
    """
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def accessions(self):
        return u"".join(ncbi.search_clone_by_name(self.name))
