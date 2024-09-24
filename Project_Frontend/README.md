<h1 align="center">Frontend para el sistema de control de asistencias con IA</h1>

## Tecnologías

Este proyecto utiliza las siguientes tecnologías:

- React 
- TypeScript
- React Query
- Tailwind CSS
- Shad CDN

## Cómo levantar el proyecto

1. Clona el repositorio.
```bash
git clone https://github.com/Duberly2004/Facial_Recognition
```
```bash
cd Facial_Recognition
```bash
cd Project_Frontend
```
2. Instala las dependencias con `npm install`.
```bash
npm install
```
3. Ejecuta el comando `npm run dev` para iniciar el servidor de desarrollo.
```bash
npm run dev
```
4. Visita `http://localhost:5173`.



     {  children: [
      {
        path: "registers",
        element: <Attendance />,
        children:[
          {
            path: "",
            element: <AttendaceList/>,
          },
          {
            path: "/registers/create",
            element: <AttendanceCreate/>,
          },
        ]
      },
      {
        path: "/users",
        element: <User />,
      },
      {
        path: "/settings",
        element: <Setting />,
        children:[
          {
            path: "/settings/departments",
            element: <Department/>,
          },
          {
            path: "/settings/positions",
            element: <Position/>,
          },
        ]
      },
    ]