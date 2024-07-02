import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { toast } from "sonner";
import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { useQueryClient } from "react-query";
import { api } from "@/services/api.service";
import { ILBase } from "@/lib/interfaces/other";
import { NameSchema } from "@/lib/validators/others";

interface Props {
  setIsPending: (value: boolean) => void;
  setIsOpen: (value: boolean) => void;
  base?: ILBase;
  setEdit?: (value: boolean) => void;
  singularName: string;
  pluralName: string;
}

export default function BaseForm({
  setIsPending,
  setIsOpen,
  base,
  setEdit,
  pluralName,
  singularName,
}: Props) {
  const queryClient = useQueryClient();

  const form = useForm<z.infer<typeof NameSchema>>({
    resolver: zodResolver(NameSchema),
    defaultValues: {
      name: base?.name ? base.name : "",
    },
  });

  const onSubmit = async (values: z.infer<typeof NameSchema>) => {
    setIsPending(true);
    try {
      if (base && base.name) {
        const res = await api.put(`/${singularName}/${base.id}`, values);
        if (setEdit) {
          setEdit(false);
        }
      } else {
        await api.post(`/${singularName}`, values);
      }
      toast.success("Todo salió con éxito ✔️ ");
      setIsOpen(false);
    } catch (error: any) {
      if (error.response && error.response.status === 400) {
        toast.error(`${error.response.data.error}`);
      } else {
        toast.error("Ocurrió un error ❌ ");
      }
    } finally {
      setIsPending(false);
      queryClient.invalidateQueries({ queryKey: pluralName });
    }
  };

  function handleFormChange(e: any) {
    if (setEdit) {
      if (e.target.value === base?.name) {
        setEdit(false); // Verificación de existencia antes de llamar a setEdit
      } else {
        setEdit(true);
      }
    }
  }

  return (
    <Form {...form}>
      <form
        onChange={setEdit ? handleFormChange : undefined}
        id={`${singularName}-form`}
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-7 w-[97%] p-[0.2rem]"
      >
        <div className="flex justify-between gap-4">
          <FormField
            control={form.control}
            name="name"
            render={({ field }) => (
              <FormItem className="w-full">
                <FormLabel>Nombre</FormLabel>
                <FormControl>
                  <Input placeholder="Escribe el nombre" {...field} />
                </FormControl>
                <FormMessage />
              </FormItem>
            )}
          />
        </div>
      </form>
    </Form>
  );
}
