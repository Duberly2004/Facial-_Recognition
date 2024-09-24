import { adminListBase } from "@/services/api.service"
import { useQuery } from "react-query"
import DataTable from "./Table"
import Loading from "@/components/Loading"

export function Teacher() {
  const getData = async ()=> await adminListBase('teachers')
  const {data,isLoading} = useQuery({queryFn:getData})
  if(isLoading) return <Loading/>
  return (
    <>
    <DataTable data={data}/>
    </>
  )
}
