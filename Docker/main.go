package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	hostname, err := os.Hostname()
	if err != nil {
		http.Error(w, "Erro ao obter o hostname", http.StatusInternalServerError)
		return
	}
	fmt.Fprintf(w, "<h1>Olá! Resposta do container Go: %s</h1>", hostname)
}

func main() {
	http.HandleFunc("/", helloHandler)

	log.Println("Servidor Go escutando na porta 8080...")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}