import { useQuery } from "react-query"
import BaseDialog from "../components/Modal"
import Table from "../components/Table"
import { listBase } from "@/services/api.service"
import Loading from "@/components/Loading"
import Error500 from "@/pages/errors/Error500"


interface Props {
    name:string
    pluralName:string
    singularName:string
  }

export default function Base({name,singularName,pluralName} : Props) {
    const fetchData = async()=>await listBase(pluralName)
    const {data,isLoading,error} = useQuery({queryKey:[pluralName],queryFn:fetchData})
    if(isLoading) return <Loading/>
    if(error) return <Error500/>
    return (
       <section className="my-7 flex justify-end">
        <BaseDialog pluralName={pluralName} singularName={singularName} name={name}  isEdit={false} />
        <div className="my-7 w-full flex justify-center flex-col">
          <Table name={name} singularName={singularName} pluralName={pluralName} data={data?data:[]}/>
        </div>
       </section>
    )
}
