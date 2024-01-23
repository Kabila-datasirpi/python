package main
 
import (
    "fmt"
    "net/http"
    "io/ioutil"
)
 
func main() {
    http.HandleFunc("/printName", printNameHandler)
    fmt.Println("Server listening on :8080")
    http.ListenAndServe(":8080", nil)
}
 
func printNameHandler(w http.ResponseWriter, r *http.Request) {
    if r.Method == "POST" {
        body, err := ioutil.ReadAll(r.Body)
        if err != nil {
            http.Error(w, "Error reading request body", http.StatusInternalServerError)
            return
        }
 
        name := string(body)
        fmt.Fprintf(w, "Hello, %s!\n", name)
    } else {
        http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)
    }
}
 