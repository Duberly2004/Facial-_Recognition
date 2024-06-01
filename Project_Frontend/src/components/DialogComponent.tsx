import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import React from "react"
interface Props {
  setOpen: (value: boolean) => void
  open: boolean
  content: React.ReactElement
  title?: string
  description?: string
  btnClose?: boolean
  btn?:React.ReactNode
}
export function BaseDialog(props: Props) {
  return (
    <Dialog open={props.open} onOpenChange={props.setOpen}>
      <DialogTrigger asChild>
        <Button variant="outline">Edit Profile</Button>
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          {props.title && (
            <DialogTitle>{props.title}</DialogTitle>
          )}
          {props.description && (
            <DialogDescription>
              {props.description}
            </DialogDescription>
          )}
        </DialogHeader>
        {props.content}
        <DialogFooter>
          {props.btn}
          {props.btnClose && (
            <DialogClose asChild>
              <Button type="button" variant="secondary">
                Cancelar
              </Button>
            </DialogClose>
          )}
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
}
