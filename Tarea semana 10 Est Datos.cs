using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using iTextSharp.text;
using iTextSharp.text.pdf;

// Definición de la clase que representa a un individuo
class Individuo
{
    private string nombrePersona; // Variable privada para almacenar el nombre del individuo

    // Constructor que asigna un nombre al individuo
    public Individuo(string nombrePersona)
    {
        this.nombrePersona = nombrePersona; // Asigna el nombre pasado como parámetro
    }

    // Método para obtener el nombre del individuo
    public string ObtenerNombre()
    {
        return nombrePersona; // Retorna el nombre almacenado del individuo
    }

    // Método para cambiar el nombre del individuo
    public void EstablecerNombre(string nuevoNombre)
    {
        nombrePersona = nuevoNombre; // Asigna un nuevo nombre al individuo
    }

    // Método que retorna el nombre del individuo cuando se imprime el objeto
    public override string ToString()
    {
        return nombrePersona; // Retorna el nombre del individuo como representación en consola
    }
}

// Definición de la clase que maneja la campaña de inmunización
class CampañaDeInmunización
{
    private List<Individuo> listaIndividuos; // Lista con todos los individuos de la campaña
    private List<Individuo> inmunizadosConPfizer; // Lista de individuos que han recibido la vacuna Pfizer
    private List<Individuo> inmunizadosConAstraZeneca; // Lista de individuos que han recibido la vacuna AstraZeneca

    // Constructor que inicializa las listas de individuos y asigna aleatoriamente a los vacunados
    public CampañaDeInmunización(int totalIndividuos, int inmunizadosConPfizer, int inmunizadosConAstraZeneca)
    {
        listaIndividuos = new List<Individuo>(); // Inicializa la lista de individuos

        // Se generan los individuos con nombres secuenciales
        for (int i = 1; i <= totalIndividuos; i++)
        {
            listaIndividuos.Add(new Individuo($"Individuo {i}")); // Añade un nuevo individuo con nombre único
        }

        // Se crea una copia de la lista para realizar selecciones aleatorias
        List<Individuo> listaSeleccionada = listaIndividuos.ToList(); 
        Random rand = new Random(); // Crea una instancia de aleatoriedad para seleccionar individuos

        // Se seleccionan aleatoriamente a los inmunizados con cada vacuna
        this.inmunizadosConPfizer = new List<Individuo>(listaSeleccionada.OrderBy(x => rand.Next()).Take(inmunizadosConPfizer));
        this.inmunizadosConAstraZeneca = new List<Individuo>(listaSeleccionada.OrderBy(x => rand.Next()).Take(inmunizadosConAstraZeneca));
    }

    // Métodos que devuelven el total de individuos y de inmunizados con cada vacuna
    public int ObtenerTotalIndividuos() => listaIndividuos.Count; // Devuelve la cantidad de individuos en la campaña
    public int ObtenerTotalInmunizadosConPfizer() => inmunizadosConPfizer.Count; // Retorna el número de inmunizados con Pfizer
    public int ObtenerTotalInmunizadosConAstraZeneca() => inmunizadosConAstraZeneca.Count; // Retorna el número de inmunizados con AstraZeneca

    // Método que retorna la lista de individuos que no están inmunizados
    public List<Individuo> ObtenerIndividuosNoInmunizados()
    {
        List<Individuo> noInmunizados = new List<Individuo>(listaIndividuos); // Se hace una copia de la lista de individuos
        noInmunizados.RemoveAll(individuo => inmunizadosConPfizer.Contains(individuo) || inmunizadosConAstraZeneca.Contains(individuo)); // Elimina los inmunizados
        return noInmunizados; // Devuelve la lista de no inmunizados
    }

    // Método que devuelve la lista de individuos que recibieron ambas dosis (intersección de las listas)
    public List<Individuo> ObtenerInmunizadosConAmbasDosis()
    {
        return inmunizadosConPfizer.Intersect(inmunizadosConAstraZeneca).ToList(); // Devuelve la intersección entre las listas de inmunizados
    }

    // Método que devuelve la lista de individuos inmunizados solo con Pfizer
    public List<Individuo> ObtenerInmunizadosSoloConPfizer()
    {
        return inmunizadosConPfizer.Except(inmunizadosConAstraZeneca).ToList(); // Devuelve los que están solo en la lista de Pfizer
    }

    // Método que devuelve la lista de individuos inmunizados solo con AstraZeneca
    public List<Individuo> ObtenerInmunizadosSoloConAstraZeneca()
    {
        return inmunizadosConAstraZeneca.Except(inmunizadosConPfizer).ToList(); // Devuelve los que están solo en la lista de AstraZeneca
    }

    // Método que genera el reporte de inmunización en formato PDF
    public void GenerarReporte()
    {
        // Llama al método estático para generar el PDF con las listas de individuos
        ReporteInmunizacion.GenerarPDF(
            ObtenerIndividuosNoInmunizados(),
            ObtenerInmunizadosConAmbasDosis(),
            ObtenerInmunizadosSoloConPfizer(),
            ObtenerInmunizadosSoloConAstraZeneca()
        );
    }
}

// Definición de la clase que crea el reporte de inmunización en formato PDF
class ReporteInmunizacion
{
    // Método que genera el reporte en un archivo PDF
    public static void GenerarPDF(List<Individuo> noInmunizados, List<Individuo> inmunizadosConAmbasDosis, List<Individuo> inmunizadosSoloConPfizer, List<Individuo> inmunizadosSoloConAstraZeneca)
    {
        string ruta = "Reporte_Inmunizacion.pdf"; // Ruta para guardar el archivo PDF generado
        Document doc = new Document(); // Se crea un documento PDF nuevo
        PdfWriter.GetInstance(doc, new FileStream(ruta, FileMode.Create)); // Establece la ubicación del archivo PDF
        doc.Open(); // Abre el documento para agregar contenido

        // Agrega las listas de individuos al PDF con sus respectivos encabezados
        AgregarListaAlPDF(doc, "Individuos NO inmunizados", noInmunizados);
        AgregarListaAlPDF(doc, "Individuos inmunizados con ambas dosis", inmunizadosConAmbasDosis);
        AgregarListaAlPDF(doc, "Individuos solo inmunizados con Pfizer", inmunizadosSoloConPfizer);
        AgregarListaAlPDF(doc, "Individuos solo inmunizados con AstraZeneca", inmunizadosSoloConAstraZeneca);

        doc.Close(); // Cierra el documento PDF
        Console.WriteLine("\nReporte PDF generado con éxito en 'Reporte_Inmunizacion.pdf'."); // Mensaje de confirmación en consola
    }

    // Método auxiliar para agregar las listas de individuos al documento PDF
    private static void AgregarListaAlPDF(Document doc, string titulo, List<Individuo> lista)
    {
        doc.Add(new Paragraph($"\n{titulo}:")); // Añade un título para cada lista
        foreach (var individuo in lista)
        {
            doc.Add(new Paragraph($"- {individuo.ObtenerNombre()}")); // Añade cada nombre de individuo en la lista
        }
    }
}

// Clase principal que ejecuta el programa
class Programa
{
    static void Main()
    {
        // Crea una instancia de la campaña de inmunización con parámetros iniciales
        CampañaDeInmunización campaña = new CampañaDeInmunización(500, 75, 75);

        // Muestra en consola el resultado de las distintas categorías
        Console.WriteLine($"Total individuos: {campaña.ObtenerTotalIndividuos()}");
        Console.WriteLine($"No inmunizados: {campaña.ObtenerIndividuosNoInmunizados().Count}");
        Console.WriteLine($"Inmunizados con ambas dosis: {campaña.ObtenerInmunizadosConAmbasDosis().Count}");
        Console.WriteLine($"Solo inmunizados con Pfizer: {campaña.ObtenerInmunizadosSoloConPfizer().Count}");
        Console.WriteLine($"Solo inmunizados con AstraZeneca: {campaña.ObtenerInmunizadosSoloConAstraZeneca().Count}");

        // Llama al método para generar el reporte en PDF
        campaña.GenerarReporte();
    }
}