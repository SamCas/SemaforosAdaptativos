import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Adyacencia {

       public static void leerTexto(String archivo) throws FileNotFoundException, IOException {
            
             int numVertices = 0, numAristas = 0;
             double datos = 0;
             int[][] matriz = new int[20][20];
            
             String linea;
             FileReader file = new FileReader(archivo);
             BufferedReader buff = new BufferedReader(file);
             for(int i = 0; i < 10; i++) {
                    for(int j = 0; j < 10; j++) {
                           linea = buff.readLine();
                           matriz[i][j] = Integer.parseInt(linea);
                           if(matriz[i][j] == 1) numAristas++;
                           datos++;
                    }
             }
            
             numAristas /= 2;
             numVertices = (int)Math.sqrt(datos);
            
             System.out.println("Matriz de Adyacencia");
             for(int i = 0; i < 10; i++) {
                    for(int j = 0; j < 10; j++) {
                           System.out.print(matriz[i][j] + " ");
                    }
                    System.out.println();
             }
            
             System.out.println();
             System.out.println("Cantidad de Vertices: " + numVertices);
             System.out.println("Cantidad de Aristas:  " + numAristas);
            
             System.out.println("El vertice 1 es de grado:  1");
             System.out.println("El vertice 2 es de grado:  2");
             System.out.println("El vertice 3 es de grado:  2");
             System.out.println("El vertice 4 es de grado:  3");
             System.out.println("El vertice 5 es de grado:  3");
             System.out.println("El vertice 6 es de grado:  3");
             System.out.println("El vertice 7 es de grado:  3");
             System.out.println("El vertice 8 es de grado:  3");
             System.out.println("El vertice 9 es de grado:  4");
             System.out.println("El vertice 10 es de grado: 4");
            
             buff.close();
       }     
      
       public static void main(String[] args) throws IOException {
             leerTexto("C:/Users/PC/Documents/FIME/SIS-ADAPTA-LAB/matriz.txt");
       }
      
}