import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import { useState } from "react";
import BaseForm from "./Form";
import { Loader2 } from "lucide-react";
import { ButtonEdit } from "@/components/Buttons";
import { ILBase } from "@/lib/interfaces/other";
interface Props {
    isEdit?:boolean //Es opcional si no se pasa sera false
    name:string
    base?:ILBase
    singularName:string
    pluralName:string
}
export default function BaseDialog({isEdit,name,base,pluralName,singularName}:Props) {
    const [isPending, setIsPending] = useState(false);
    const [isOpen, setIsOpen] = useState(false);
  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        {isEdit?
        <ButtonEdit onClick={() => null} />
        :<Button className="bg-sky-500 hover:bg-sky-600" size={"sm"}>Nuevo</Button>}
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>{name} / {isEdit?"Editar":"Crear"}</DialogTitle>
        </DialogHeader>
        <div className="grid gap-4 py-4">
            <BaseForm pluralName={pluralName} singularName={singularName} base={base} setIsPending={setIsPending} setIsOpen={setIsOpen}/>
        </div>
        <DialogFooter>
          <Button disabled={isPending} className="bg-sky-600 hover:bg-sky-700" form={`${singularName}-form`} type="submit">
            {isPending?
            <Loader2 className="animate-spin"/>:null}
            {isEdit?"Guardar cambios":"Crear"} 
            </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
