
/**
   Interface para representar soluciones que pueden ser usadas
   en el metodo de recocido simulado

   @author Benjamin Torres
   @version 0.1
*/
package recocido;
public class Solucion{
    
    float valor; //valor de la solucion actual

    /**
       Metodo constructor de una solucion a un problema
    */
    public Solucion(){
        this.valor=0;
    }

    /**
       Genera, a partir de una aproximacion de solucion una
       nueva dentro de la vecindad actual
       @return genera una solucion nueva basada en la que llama al método
    */
    public Solucion siguienteSolucion(){
        return new Solucion();
    }

    /**
       Asigna un valor a la solucion que invoca el metodo
       @return evaluacion de la solucion
    */
    public float evaluar(){
        return 0;
    }

    /**
       Metodo para imprimir a una solucion
       @return Representacion de cadena para la solucion
    */
    public String toString(){
        return "Solucion:";
    }
}
