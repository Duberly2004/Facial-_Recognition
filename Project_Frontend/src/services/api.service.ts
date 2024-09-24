import { ERoute } from "@/lib/enums";
import { IBase } from "@/lib/interfaces/other";
import axios from "axios";

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const adminListBase = async(listName:string)=>await listBase(ERoute.ADMIN +"/"+ listName)
export const teacherListBase = async(listName:string)=>await listBase(ERoute.TEACHER +"/"+ listName)
export const studentListBase = async(listName:string)=>await listBase(ERoute.STUDENT +"/"+ listName)

//-------Base--------------
export const listBase = async (listName:string)=>{
    const {data} = await api.get(`/${listName}`)
    return data
}
export const createBase = async (createName:string,base:IBase)=>{
  const {data} = await api.post(`/${createName}`,base)
  return data
}
export const updateBase = async (updateName:string,id:number,base:IBase)=>{
  const {data} = await api.post(`/${updateName}/${id}`,base)
  return data
}
export const deleteBase = async (deleteName:string,id:number)=>{
  const {data} = await api.delete(`/${deleteName}/${id}`)
  return data
}