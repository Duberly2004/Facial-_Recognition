import { Separator } from "@/components/ui/separator"
import { Card,CardContent } from "@/components/ui/card"
interface TeacherCourse {
  id:number
  name:string
  section_name:string
}
const list_teacher_courses:TeacherCourse[] = [
  {id:1,name:"Desarrollo de Aplicaciones Empresariales Avanzado",section_name:"Sección: C24 - 6 - A"},
  {id:1,name:"Desarrollo de Aplicaciones Empresariales Avanzado",section_name:"Sección: C24 - 6 - B"},
  {id:2,name:"Aplicaciones Móviles Multiplataforma",section_name:"Sección: C24 - 5 - A"},
  {id:2,name:"Programación Orientada a Objetos",section_name:"Sección: C24 - 2 - A"},
] 
export function SeparatorDemo({course}:{course:TeacherCourse}) {
  return (
    <Card>
      <CardContent>
      <div className="space-y-1 pt-4">
        <h4 className="text-sm font-medium leading-none">{course.section_name}</h4>
        <p className="text-sm text-muted-foreground">
          {course.name}
        </p>
      </div>
      <Separator className="my-4" />
      <div className="flex h-5 items-center space-x-4 text-sm">
        <div className="hover:underline hover:cursor-pointer hover:font-bold">Registros</div>
        <Separator orientation="vertical" />
        <div className="hover:underline hover:cursor-pointer hover:font-bold">Alumnos</div>
        <Separator orientation="vertical" />
        <div className="hover:underline hover:cursor-pointer hover:font-bold">Cámara</div>
      </div>
      </CardContent>
    </Card>
  )
}

export default function Courses() {
  return (
    <div className="flex gap-4 mt-5 flex-wrap">
      {list_teacher_courses.map(item=>(
        <SeparatorDemo course={item}/>
      ))}
    </div>
  )
}
