"use client"

import { zodResolver } from "@hookform/resolvers/zod"
import { useForm } from "react-hook-form"
import { z } from "zod"

import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { toast } from "sonner"
import BaseSelect from "@/components/selects/BaseSelect"
import React from "react"
import { useQueryClient } from "react-query"
import { api } from "@/services/api.service"
import { Input } from "@/components/ui/input"
const FormSchema = z.object({
  date: z.string({
    required_error: "La fecha es requerida",
  }),
  course_id: z.number({ required_error: "El curso es requerido" }),
  career_id: z.number({ required_error: "La carrera es requerida" }),
  section_id: z.number({ required_error: "La sección es requerido" }),
})

export default function AttendaceForm() {
  const [careerId, setCareerId] = React.useState<number>()
  const [loading, setLoading] = React.useState<boolean>(false)
  const queryClient = useQueryClient();
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
  })

  async function onSubmit(data: z.infer<typeof FormSchema>) {
    setLoading(true)
    console.log(data)
    try {
      const response = await api.post('attendance',data)
      window.localStorage.setItem('attendanceId',response.data.id)
      toast.success("Asistencia creada correctamente")
    } catch (error) {
      toast.error('Error al crear la asistecia')
    } finally {
      setLoading(false);
      queryClient.invalidateQueries({ queryKey: "attendances" });
    }
  }

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="flex items-center gap-2">
        <FormField
          control={form.control}
          name="date"
          render={({ field }) => (
            <FormItem className="flex flex-col">
              <FormLabel>Fecha</FormLabel>
              <FormControl>
                <Input
                  type="date"
                  onChange={field.onChange}
                  />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="career_id"
          render={({ field }) => (
            <FormItem className="flex flex-col">
              <FormLabel>Carrera</FormLabel>
              <FormControl>
                <BaseSelect name="Seleccione" onChange={(e) => {
                  setCareerId(e)
                  field.onChange(e)
                }} pluranName="careers" />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="section_id"
          render={({ field }) => (
            <FormItem className="flex flex-col">
              <FormLabel>Sección</FormLabel>
              <FormControl>
                <BaseSelect name="Seleccione" onChange={field.onChange} pluranName={`career/${careerId}/sections`} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="course_id"
          render={({ field }) => (
            <FormItem className="flex flex-col">
              <FormLabel>Curso</FormLabel>
              <FormControl>
                <BaseSelect name="Seleccione" onChange={field.onChange} pluranName={`career/${careerId}/courses`} />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button disabled={loading} className="mt-5" type="submit">Cre{loading ? "ando" : "ar"}</Button>
        {/* <img src="http://127.0.0.1:5000/video_feed" alt=""/> */}
      </form>
    </Form>
  )
}

