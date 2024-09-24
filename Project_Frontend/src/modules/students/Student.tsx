import { adminListBase } from "@/services/api.service"
import { useQuery } from "react-query"
import DataTable from "./Table"
import Loading from "@/components/Loading"

export function Student() {
  const getData = async ()=> await adminListBase('students')
  const {data,isLoading} = useQuery({queryFn:getData})
  if(isLoading) return <Loading/>
  return (
    <>
    <DataTable data={data}/>
    </>
  )
}
