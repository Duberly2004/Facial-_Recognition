import BaseSelect from "@/components/selects/BaseSelect";
import { Button } from "@/components/ui/button";
import { deleteBase, listBase } from "@/services/api.service";
import { useQuery, useQueryClient } from "react-query";
import { toast } from "sonner";
import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableFooter,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { ILRegister } from "@/lib/interfaces/other";
import { convertDate } from "@/lib/functions/convert";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { ButtonDelete } from "@/components/Buttons";

export default function AttendaceList({show=true}:{show?:boolean}) {
  const fetchData = async () => await listBase("registers");
  const queryClient = useQueryClient()
  const { data, isLoading } = useQuery({queryKey:"registers",queryFn:fetchData});
  if (isLoading) return <p>Cargando</p>
  async function onDelete(id:number){
    try {
      await deleteBase(`register`,id)
      toast.success("Eliminado correctamente")
    } catch (error) {
      toast.error("Ocurrión un error")
    }finally{
      queryClient.invalidateQueries({queryKey:"registers"})
    }
  }
  return (
    <div>
      {show&&(
        <div className="flex gap-1">
        <BaseSelect name="Departamentos" onChange={(e) => console.log(e)} pluranName={`departments`} />
        <BaseSelect name="Cargo" onChange={(e) => console.log(e)} pluranName={`positions`} />
        <Button onClick={()=>toast.success("Buscado exitosamente")}>Buscar</Button>
        </div>
      )}
      {data ?
        <Table>
          <TableCaption>Lista de registros</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">#</TableHead>
              <TableHead>Nombre</TableHead>
              <TableHead>Departamento</TableHead>
              <TableHead>Rol</TableHead>
              <TableHead>Fecha</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((register: ILRegister, index: number) => (
              <TableRow key={register.id}>
                <TableCell className="font-medium">{index + 1}</TableCell>
                <TableCell className="font-medium">{register.user.name} {register.user.paternal_surname} {register.user.maternal_surname}</TableCell>
                <TableCell>{register.user.department.name}</TableCell>
                <TableCell>{register.user.position.name}</TableCell>
                <TableCell>{convertDate(register.date.toString())}</TableCell>
                <TableCell>
                  <Avatar>
                      <AvatarImage src={register.user.profile_picture_url} alt="@shadcn" />
                      <AvatarFallback>CN</AvatarFallback>
                  </Avatar>
                  </TableCell>
                  <TableCell><ButtonDelete onClick={()=>onDelete(register.id)}/></TableCell>
              </TableRow>
            ))}
          </TableBody>
          <TableFooter>
            <TableRow>
              <TableCell colSpan={6}>Total</TableCell>
              <TableCell className="text-right">{data.length}</TableCell>
            </TableRow>
          </TableFooter>
        </Table>
        : <p className="text-center text-sm mt-4 text-gray-700">Seleccione el departmento o cargo para filtrar registros</p>}

    </div>
  )
}