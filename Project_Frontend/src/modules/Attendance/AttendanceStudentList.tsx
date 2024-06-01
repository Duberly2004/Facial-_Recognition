import { listBase } from '@/services/api.service';
import { useQuery } from 'react-query';
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
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

interface Props {
    attendaceId: number
}
export default function AttendanceStudentList({ attendaceId }: Props) {
    const fetchData = async () => await listBase(`attendances/${attendaceId}/attendancesStudents`);
    const { data, isLoading } = useQuery({ queryKey: ['attendacesStudents'], queryFn: fetchData });
    if (isLoading) return <p>Cargando</p>;
    return (
        <Table>
            <TableCaption>Lista de asistencia de los estudiantes</TableCaption>
            <TableHeader>
                <TableRow>
                    <TableHead>#</TableHead>
                    <TableHead>Nombre</TableHead>
                    <TableHead>Asistencia</TableHead>
                    <TableHead>Foto</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                {data.map((item: any, index: number) => (
                    <TableRow key={index}>
                        <TableCell>{index + 1}</TableCell>
                        <TableCell>{item.name} {item.paternal_surname} {item.maternal_surname}</TableCell>
                        <TableCell>{item.status}</TableCell>
                        <TableCell>
                            <Avatar>
                                <AvatarImage src={import.meta.env.VITE_API_URL + "/"+ item.avatar} alt="@shadcn" />
                                <AvatarFallback>CN</AvatarFallback>
                            </Avatar>
                            </TableCell>
                    </TableRow>
                ))}
            </TableBody>
            <TableFooter>
                <TableRow>
                    <TableCell colSpan={3}>Total</TableCell>
                    <TableCell className="text-right">{data.length}</TableCell>
                </TableRow>
            </TableFooter>
        </Table>
    )
}