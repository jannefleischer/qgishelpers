from PyQt4.QtGui import *
from qgis.gui import *
composers = iface.activeComposers()
#print composers
diag = QDialog()
listW = QListWidget()
lay = QVBoxLayout()
for f in composers:
    listW.addItem(f.composerWindow().windowTitle())
listW.setSortingEnabled(True)
listW.sortItems()
lay.addWidget(listW)
box = QDialogButtonBox()
box.addButton(QDialogButtonBox.Ok)
box.addButton(QDialogButtonBox.Cancel)
lay.addWidget(box)
diag.setLayout(lay)
box.button(QDialogButtonBox.Ok).clicked.connect(lambda: diag.accept() )
box.button(QDialogButtonBox.Cancel).clicked.connect(lambda: diag.reject() )
result = diag.exec_()
print result
if result == 1:
    for f in composers:
        if (f.composerWindow().windowTitle()== listW.currentItem().text() ):
            maps = QgsMapLayerRegistry.instance().mapLayers()
            for mapname, map in maps.iteritems():
                iface.legendInterface().setLayerVisible(map, False)
            for m in f.composition().composerMapItems():
                layerset = m.layerSet()
                for l in layerset:
                    iface.legendInterface().setLayerVisible(maps[l], True)
        else:
            continue
elif not result:
    pass

