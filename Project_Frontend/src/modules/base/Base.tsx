import { listBase } from "@/services/api.service"
import { useQuery } from "react-query"
import DataTable from "./Table"
import Loading from "@/components/Loading"

export default function Base({endpointName}:{endpointName:string}) {
  const getData = async ()=> await listBase(endpointName)
  const {data,isLoading} = useQuery({queryFn:getData,queryKey:endpointName})
  if(isLoading) return <Loading/>
  return (
    <DataTable data={data}/>
  )
}
