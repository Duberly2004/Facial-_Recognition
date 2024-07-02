export const getNameStatus=(value:number)=>{
    switch (value) {
        case 0:
            return "Activo"
        case 1:
            return "Inactivo"
        case 2:
            return "Suspendido"
        default:
            return ""
    }
}