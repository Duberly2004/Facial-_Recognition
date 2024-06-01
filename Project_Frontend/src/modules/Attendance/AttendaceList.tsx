import BaseSelect from "@/components/selects/BaseSelect";
import { Button } from "@/components/ui/button";
import { listBase } from "@/services/api.service";
import React from "react";
import { useQuery } from "react-query";
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
import { ILattendace } from "@/lib/interfaces/other";
import { convertDate } from "@/lib/functions/convert";
export default function AttendaceList() {
  const [careerId, setCareerId] = React.useState<number | undefined>();
  const [sectionId, setSectionId] = React.useState<number | undefined>();
  const [courseId, setCourseId] = React.useState<number | undefined>();
  const [endpoint, setEndpoint] = React.useState<string>("");

  const fetchData = async () => await listBase(endpoint);

  const { data, isLoading } = useQuery(["attendances", endpoint], fetchData, {
    enabled: !!endpoint, // solo habilita la consulta cuando el endpoint está definido
  });

  const onSearch = () => {
    if (careerId !== undefined && sectionId !== undefined && courseId !== undefined) {
      setEndpoint(`section/${sectionId}/course/${courseId}/attendances`);
    } else {
      toast.error('Llene todos los campos');
    }
  };
  if (isLoading) return <p>Cargando</p>

  return (
    <div>
      <div className="flex gap-1">
        <BaseSelect name="Carrera" onChange={(e) => setCareerId(e)} pluranName={`careers`} />
        <BaseSelect name="Sección" onChange={(e) => setSectionId(e)} pluranName={`career/${careerId}/sections`} />
        <BaseSelect name="Cursos" onChange={(e) => setCourseId(e)} pluranName={`career/${careerId}/courses`} />
        <Button onClick={onSearch}>Buscar</Button>
      </div>
      {data ?
        <Table>
          <TableCaption>Lista de asistencias</TableCaption>
          <TableHeader>
            <TableRow>
              <TableHead className="w-[100px]">#</TableHead>
              <TableHead>Carrera</TableHead>
              <TableHead>Sección</TableHead>
              <TableHead>Curso</TableHead>
              <TableHead>Fecha</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {data.map((attedace: ILattendace, index: number) => (
              <TableRow key={attedace.id}>
                <TableCell className="font-medium">{index + 1}</TableCell>
                <TableCell className="font-medium">{attedace.career_id}</TableCell>
                <TableCell>{attedace.section_id}</TableCell>
                <TableCell>{attedace.course_id}</TableCell>
                <TableCell>{convertDate(attedace.date.toString())}</TableCell>
              </TableRow>
            ))}
          </TableBody>
          <TableFooter>
            <TableRow>
              <TableCell colSpan={4}>Total</TableCell>
              <TableCell className="text-right">{data.length}</TableCell>
            </TableRow>
          </TableFooter>
        </Table>
        : <p className="text-center text-sm mt-4 text-gray-700">Seleccione la carrera, sección y curso para buscar las asistencias</p>}

    </div>
  )
}