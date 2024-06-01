export const getNameStatus=(value:string)=>{
    switch (value) {
        case "ACTIVE":
            return "Activo"
        case "INACTIVE":
            return "Inactivo"
        case "SUSPENDED":
            return "Suspendido"
        default:
            return ""
    }
}