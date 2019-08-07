package ia;

import processing.core.PApplet;
import processing.core.PFont;

import java.util.Stack;
import java.util.ArrayList;
import java.util.Random;

public class Laberinto extends PApplet{

    PFont fuente;

    // Propiedades del modelo de laberinto.
    int alto = 15;         // Altura (en celdas) de la cuadricula.
    int ancho = 15;        // Anchura (en celdas) de la cuadricula.
    int celda = 30;          // Tamanio de cada celda cuadrada  (en pixeles).
    ModeloLaberinto modelo;  // El objeto que representa el modelo laberinto.

    /**
     * Setup
     */
    @Override
    public void setup () {
        size(ancho*celda,  alto*celda);
        background(255);
        frame.setResizable(true);
        fuente = createFont("Arial", 12, true);
        modelo = new ModeloLaberinto (ancho, alto, celda);
    }

    /**
     * Pintar el mundo del modelo  (la cuadricula).
     */
    @Override
    public void draw() {
        fill(255,0,0); //cuadrado rojo que recorre

        noStroke();
        rect(modelo.current.celdaX*modelo.size,  modelo.current.celdaY*modelo.size,  modelo.size,  modelo.size);
        stroke(0);
        //Se dibujan las lineas
        //line(x1,y1,   x2,y2)
        //recorremos la matriz
        for (int i = 0; i < alto; i++)
            for (int j = 0; j < ancho; j++){
                if (modelo.world[i][j].up){
                    //pintamos arriba
                    line(j*modelo.size, i*modelo.size, (j + 1)*modelo.size, i*modelo.size);
                    stroke(0);
                }
                if (modelo.world[i][j].right){
                    //pintamos a la derecha
                    line((j+1)*modelo.size, i*modelo.size, (j+1)*modelo.size, (i+1)*modelo.size);
                    stroke(0);
                }
                if (modelo.world[i][j].left){
                    line((j)*modelo.size, i*modelo.size, (j)*modelo.size, (i+1)*modelo.size);
                    stroke(0);
                }
            }

        //metodo que realiza el laberinto
        modelo.backtrack();
    }


    /**
     * Clase celda
     * tiena tributo posicion (x,y).
     * Valores de visitado
     * Y nos dice si tiene vecinos arriba, abajo, derecha e izquierda
     */
    class Celda{
        int celdaX, celdaY; //posición
        boolean state; //si fue visitada
        boolean up, down, right, left; //vecinos

        /**constructor sin parámetros*/
        Celda (){}
        /**constructor que recibe la posición (x,y) y el estado de si está
         * o no visitado*/
        Celda(int celdaX, int celdaY, boolean state){
            this.celdaX = celdaX;
            this.celdaY = celdaY;
            this.state = state;
            this.up = true;
            this.down = true;
            this.right = true;
            this.left = true;
        }

        /**
         * método toString se hizo para ver a mano que hace lo que debe de hacer.
         */
        @Override
        public String toString(){
            return String.format("(%d, %d)", this.celdaY, this.celdaX);
        }

        /**
         * Método equals compara coordenada a coordenada.
         */
        public boolean equals(Celda c){
            this.toString();
            c.toString();
            return this.celdaX == c.celdaX && this.celdaY == c.celdaY;
        }
    }

    /**
     * Clase laberinto, es la que crea el laberinto.
     */
    class ModeloLaberinto{
        int high, width; //tamaño de celdas alto y ancho.
        int size; //tamaño de la celda.
        Celda[][] world; //Mundo de celdas a mover.
        Stack<Celda> stack; //Stack para backtrack
        Random rnd = new Random(); //random
        Celda current;

        /**
         * Constructor de la clase.
         * inicializa el stack, le mete una celda aleatoria
         */
        ModeloLaberinto(int width, int high, int size){
            this.width = width;
            this.high = high;
            this.size = size;
            world = new Celda[high][width];
            //Inicializar el mundo.
            for (int i = 0; i < high; i++)
                for (int j = 0; j < width; j++)
                    world[i][j] = new Celda(j, i, false);
            //Stack
            stack = new Stack<>();
            //Celda aleatoria.
            int rndH = rnd.nextInt(high);
            int rndW = rnd.nextInt(width);
            current = world[rndH][rndW];
            current.state = true;
            stack.push(current);
        }
        /**
         * Nos regresa una lista con los vecinos disponibles
         */
        ArrayList<Celda> disponibles(Celda current){
            ArrayList<Celda> ngbs =  new ArrayList<>();
            if (current.celdaY - 1 >= 0)
                if (!world[current.celdaY - 1][current.celdaX].state)
                    ngbs.add(world[current.celdaY - 1][current.celdaX]);
            if (current.celdaY + 1 < high)
                if (!world[current.celdaY + 1][current.celdaX].state)
                    ngbs.add(world[current.celdaY + 1][current.celdaX]);
            if (current.celdaX - 1 >= 0)
                if (!world[current.celdaY][current.celdaX - 1].state)
                    ngbs.add(world[current.celdaY][current.celdaX - 1]);
            if (current.celdaX + 1 < width)
                if (!world[current.celdaY][current.celdaX + 1].state)
                    ngbs.add(world[current.celdaY][current.celdaX + 1]);
            return ngbs;
        }
        /**
         * Como elegimos una dirección aleatoria no sabemos a donde nos movimos.
         * así que comparamos con sus vecinos para ver cuál era.
         * Preguntamos si se puede mover a los extremos para no salirnos del array
         */
        int direccion(Celda wen){
            int dir = -1;
            if (current.celdaY - 1 >= 0)//up
                if (world[current.celdaY - 1][current.celdaX].equals(wen)) dir = 0;
            if (current.celdaY + 1 < high)
                if (world[current.celdaY + 1][current.celdaX].equals(wen)) dir = 1;
            if (current.celdaX - 1 >= 0)//left
                if (world[current.celdaY][current.celdaX - 1].equals(wen)) dir = 2;
            if (current.celdaX + 1 < width)
                if (world[current.celdaY][current.celdaX + 1].equals(wen)) dir = 3;
            System.out.println(dir);
            return dir;
        }
        /**
         * Método que borra una pared, recibe la celda vecina a current
         * dependiendo de la dirección es que borra los dos atributos de
         * las posiciones current y wen
         */
        //void borraPared(Celda wen){
        void borraPared(Celda wen){            
            int dir = direccion(wen);
            switch (dir){
            case 0://up
                current.up = false;
                wen.down = false;
                System.out.println("up");
                break;
            case 1:
                current.down = false;
                wen.up = false;
                System.out.println("down");
            case 2://left
                current.left = false;
                wen.right = false;
                System.out.println("left");
                break;
            case 3://right
                current.right = false;
                wen.left = false;   
                System.out.println("right");
                break;
            }
            //return nueva;

        }

        /**
         * metodo que hace backtrack
         */
        void backtrack(){           
            ArrayList<Celda> neighbors = new ArrayList<>();//disponibles(this.current);

            do {
                //calculamos los vecinos
                neighbors = disponibles(this.current);
                System.out.println(current);
                //verificamos que sea un número válido
                if (neighbors.size() == 0)
                    break;
                int r = rnd.nextInt(neighbors.size());
                if (neighbors.size() == 0) break;
                //nuestra celda vecina
                Celda wen = neighbors.get(r);
                //esto borra la celda vecina para ya no volver a visitarla
                //neighbors.remove(r);
                wen.state = true; //actualizar estado
                //borrar pared
                //wen = borraPared(wen);
                borraPared(wen);
                //actualizar referencias
                this.current = wen;
                //meter al stack
                stack.push(wen);

                //do while para poder entrar al while sin tener la lista inicializada
            } while (neighbors.isEmpty());


            if (neighbors.isEmpty())
                if (!this.stack.empty()){
                    //si llegamos aquí es porque no tenemos a donde movernos
                    //sacamos de la pila el último elemento.
                    Celda prev = this.stack.pop();
                    this.current = prev;
                }       
             
        }

    }

    public static void main (String[] args) {
        PApplet.main (new String[] { "ia.Laberinto" });
    }
}


