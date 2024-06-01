export const convertDate = (dateString: string): string => {
    const dateObject = new Date(dateString);
    const options: Intl.DateTimeFormatOptions = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric',
        timeZone: 'UTC'
    };
    return dateObject.toLocaleString('es-ES', options);
}