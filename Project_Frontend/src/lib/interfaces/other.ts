export interface IBase {
    name:string
}
export interface ILBase extends IBase {
    id:number
}

export interface IRegister {
    date: string,
}
export interface ILRegister extends IRegister {
    id:number
    user:ILUser
}
export interface IUser {
    email:string
    password:string
    profile_picture_url:string
    name:string
    paternal_surname:string
    maternal_surname:string
    status:number
    
}
export interface ILUser extends IUser {
    id:number
    role:ILBase
    position:ILBase
    department:ILBase
}