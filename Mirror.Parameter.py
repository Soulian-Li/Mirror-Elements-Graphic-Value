"""
__author__ = 'Soulian Li'
__Gmail__ = 'liang.li1104@gmail.com'
__version__ = '1.0.0'
__Date__ = '07.04.20'

"""

from RevitServices.Transactions import TransactionManager
from Autodesk.DesignScript.Geometry import *
from RevitServices.Persistence import DocumentManager
import RevitServices
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB import *
import clr
import sys
# import Revit API
clr.AddReference('RevitAPI')
# import Revit API UI
clr.AddReference('RevitAPIUI')
# import Revit Services
clr.AddReference('RevitServices')
# import ProtoGeometry
clr.AddReference('ProtoGeometry')
# get Revit's current Document file.
doc = DocumentManager.Instance.CurrentDBDocument
# get the current application
app = DocumentManager.Instance.CurrentUIApplication.Application
# get the user interface application
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application


# Dynamo input
elements = IN[0]
Mparameter = IN[1]

# Empty list
value = []
# loop over elements
for e in UnwrapElement(elements):
    # look up parameter
    p = e.GetParameters(Mparameter)
    # start Revit transaction
    TransactionManager.Instance.EnsureInTransaction(doc)

    # look up parameter
    for i in p:
        # set parameter.
        ii = i.AsDouble()
        value.append(ii)
        i.Set(-1*ii)
        # end Revit transaction
    TransactionManager.Instance.TransactionTaskDone()
OUT = map(lambda x: x*-304.8, value)
