import React from 'react'
import AttendaceForm from './AttendaceForm'
import { listBase } from '@/services/api.service';
import { useQuery } from 'react-query';
import { convertDate } from '@/lib/functions/convert';
import AttendanceStudentList from './AttendanceStudentList';

export default function AttendanceCreate() {
  const [endpoint, setEndpoint] = React.useState<string>("");

  const id = window.localStorage.getItem('attendanceId')
  const fetchData = async () => await listBase(endpoint);

  const { data, isLoading } = useQuery(["attendances", endpoint], fetchData, {
    enabled: !!endpoint, // solo habilita la consulta cuando el endpoint está definido
  });

  if (isLoading) return <p>Cargando</p>
  if(id && !data) {
    setEndpoint(`attendance/${id}`)
    console.log(id)
  }
  console.log(data)
  return (
    <div>
      <AttendaceForm/>
      {data&&(
        <div>
          <p className='my-3'>Fecha: {convertDate(data.date)}</p>
          <img src={`${import.meta.env.VITE_API_URL}/video_feed/${id}`} alt="" />
          <AttendanceStudentList attendaceId={data.id}/>
        </div>
      )}
    </div>
  )
}
