/**
   Clase para ejecutar un proceso de optimizacion usando recocido simulado
   @author Benjamin Torres Saavedra
   @version 0.1
*/
package recocido;
import static java.lang.System.out;

public class Main{
    public static void main(String []args){
        int interaciones = 100;
        RecocidoSimulado recocido = new RecocidoSimulado();
        Solucion s = recocido.ejecutar();
        out.println(s);
    }
}
