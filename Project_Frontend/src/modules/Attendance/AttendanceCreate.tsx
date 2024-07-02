import { listBase } from '@/services/api.service';
import { useQuery } from 'react-query';
import { convertDate } from '@/lib/functions/convert';
import Error500 from '@/pages/errors/Error500';
import AttendaceList from './AttendaceList';

export default function AttendanceCreate() {
  const fetchData = async () => await listBase("registers");
  const { data, isLoading,error } = useQuery(["registers"], fetchData);
  const date = new Date()
  if (isLoading) return <p>Cargando</p>
  if(error) return <Error500/>
  return (
    <div>
      {data&&(
        <div>
          <p className='my-3'>Fecha: {convertDate(date.toString())}</p>
          <img src={`${import.meta.env.VITE_API_URL}/video_feed`} alt="" />
          <AttendaceList show={false}/>
        </div>
      )}
    </div>
  )
}
