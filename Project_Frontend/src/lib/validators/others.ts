import { z } from "zod";

export const NameSchema = z.object({
    name: z.string().min(1, "Ingrese una categoría válida 😒"),
  });