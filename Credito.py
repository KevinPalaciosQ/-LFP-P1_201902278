class Creditos:
    def __init__(self,codigo,nombre,obligatorio,semestre,creditos,estado):
        self.codigo=codigo
        self.nombre=nombre
        self.prerrequisitos=[]
        self.obligatorio=obligatorio
        self.semestre=semestre
        self.creditos=creditos
        self.estado=estado
    
    def getCodigo(self):
        return self.codigo
    def getNombre(self):
        return self.nombre
    def getObligatorio(self):
        return self.obligatorio
    def getSemestre(self):
        return self.semestre
    def getCreditos(self):
        return self.creditos
    def getEstado(self):
        return self.estado
    def setCodigo(self, codigo):
        self.codigo = codigo
    def setNombre(self, nombre):
        self.nombre=nombre
    def setObligatorios(self, obligatorios):
        self.obligatorios=obligatorios
    def setSemestre(self, semestre):
        self.semestre=semestre
    def setCreditos(self,creditos):
        self.creditos=creditos
    def setEstado(self, estado):
        self.estado=estado



