import { Input } from "@/components/ui/input";
import React from "react";
import DataTable, { createTheme } from "react-data-table-component";
import BaseDialog from "./Modal";
import { toast } from "sonner";
import { useQueryClient } from "react-query";
import { deleteBase } from "@/services/api.service";
import { ILBase } from "@/lib/interfaces/other";
import { ButtonDelete } from "@/components/Buttons";
interface Props {
  data: ILBase[];
  name:string
  singularName:string
  pluralName:string
}

function Table({ data ,name,singularName,pluralName}: Props) {
  const [filteredRecords, setFilteredRecords] = React.useState(data);
  const queryClient = useQueryClient();

  // Actualizar los datos filtrados cuando data cambie
  React.useEffect(() => {
    setFilteredRecords(data);
  }, [data]);

  const handleDelete = async (row:ILBase) => {
    alert(`Estas seguro de eliminar a ${row.name}`)
    try {
      await deleteBase(singularName,row.id)
      toast.success("Todo salió con éxito ✔️ ")
    } catch (error) {
      toast.error("Ocurrio un error")
    }finally{
      // Invalidar la consulta para que se actualice
      queryClient.invalidateQueries({queryKey:pluralName});
    }
  }

  let columns = [
    { name: "Nombre", selector: (row: ILBase) => row.name },
    {
      name: "Acciones",
      cell: (row: ILBase) => (
        <div>
          <ButtonDelete onClick={() => handleDelete(row)} />
          <BaseDialog 
          singularName={singularName} 
          pluralName={pluralName} 
          name={name} 
          isEdit={true} 
          base={row}/>
        </div>
      ),
    },
  ];

  createTheme('dark', {
    background: {
      default: 'transparent',
    },
    text:"dark",
  });

  return (
    <section className="w-full text-black dark:text-white">
      <Input  className="placeholder:text-sm px-2 my-3" placeholder="Filtrar por nombre" type="search" onChange={(e)=>{
        const filteredRecords = data.filter((item) => item.name && item.name.toLowerCase().includes(e.target.value.toLowerCase()));
        setFilteredRecords(filteredRecords);
      }}/>

      <DataTable
        columns={columns}
        data={filteredRecords}
        fixedHeader
        theme="dark"
        customStyles={{head:{style:{background:"#00b1f7",color:"white"}}}}
      />
    </section>
  );
}


export default Table;
