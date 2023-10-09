#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Node
{
public:
int data;
Node* left;
Node* right;
Node(int data)
{
this->data = data;
this->left = nullptr;
this->right = nullptr;
}
static vector<int> lista;
};
vector<int> Node::lista;
Node* insert(Node* root, int data)
{
if (root == nullptr)
{
return new Node(data);
}
else
{
if (data == root -> data)
{
cout << "El valor " << data << " ya existe" << endl;
}
else if(data > root -> data){
root -> right = insert(root->right,data);
}
else if(data < root -> data){
root -> left = insert(root->left, data);
}
}
return root;
}
void preorden(Node* root){
if (root){
cout << root->data << endl;
preorden(root->left);
preorden(root->right);
}
}
void postorden(Node* root){
if (root){
postorden(root->left);
postorden(root->right);
cout << root->data << endl;
}
}
void simetrico(Node* root){
if (root){
simetrico(root -> left);
cout << root -> data << endl;
simetrico(root -> right);
}
}
void lista_simetrica(Node* root){
if (root){
lista_simetrica(root -> left);
Node::lista.push_back(root->data);
lista_simetrica(root -> right);
}
}
bool busqueda(const vector<int>& array, int item) {
int longitud = array.size() / 2;
if (array.size() == 1 && array[0] != item) {
return false;
}
if (array[longitud] == item) {
return true;
}
if (array[longitud] > item) {
vector<int> nuevoArray(array.begin(), array.begin() + longitud);
return busqueda(nuevoArray, item);
}
if (item > array[longitud]) {
vector<int> nuevoArray(array.begin() + longitud, array.end());
return busqueda(nuevoArray, item);
}
return false;
}
void Eliminar(Node* &root, int valor) {
if (root == nullptr) {
return;
}
if (valor < root->data) {
Eliminar(root->left, valor);
} else if (valor > root->data) {
Eliminar(root->right, valor);
} else {
// Caso 1: El nodo es una hoja
if (root->left == nullptr && root->right == nullptr) {
delete root;
root = nullptr;
}
// Caso 2: El nodo tiene un solo hijo
else if (root->left == nullptr) {
Node* temp = root;
root = root->right;
delete temp;
} else if (root->right == nullptr) {
Node* temp = root;
root = root->left;
delete temp;
}
// Caso 3: El nodo tiene dos hijos
else {
Node* temp = root->right;
while (temp->left != nullptr) {
temp = temp->left;
}
root->data = temp->data;
Eliminar(root->right, temp->data);
}
}
}
int main() {
Node* root = nullptr;
int nodos;
int elemento;
int orden;
int decision;
int elementoBuscar;
do {
cout << "Â¿Cuantos nodos tendra tu arbol? ";
cin >> nodos;
for(int i = 0; i < nodos; i++){
cout << "ingresa el elemento: ";
cin >> elemento;
root = insert(root, elemento);
}
lista_simetrica(root);
do {
cout << "Â¿Que deseas hacer? (ingresa el numero correspondiente al orden)" << endl;
cout << "1 - Recorrer el arbol" << endl;
cout << "2 - Buscar un elemento en el arbol" << endl;
cout << "3 - Eliminar un elemento del arbol" << endl;
cout << "4 - Salir" << endl;
cin >> decision;
switch (decision) {
case 1:
cout << "Â¿En que recorrido quieres que se muestre el arbol? (ingresa el numero correspondiente al orden)" << endl;
cout << "1 - Preorden" << endl;
cout << "2 - Postorden" << endl;
cout << "3 - Simetrico" << endl;
cin >> orden;
switch (orden) {
case 1:
cout << "Preorden:" << endl;
preorden(root);
break;
case 2:
cout << "Postorden:" << endl;
postorden(root);
break;
case 3:
cout << "SimÃ©trico:" << endl;
simetrico(root);
break;
default:
cout << "Ingresa un valor valido." << endl;
}
break;
case 2:
cout << "Elemento a buscar: ";
cin >> elementoBuscar;
if (busqueda(Node::lista, elementoBuscar)){
cout << "El elemento " << elementoBuscar << " estÃ¡ en el Ã¡rbol." << endl;
}else{
cout << "El elemento " << elementoBuscar << " no estÃ¡ en el Ã¡rbol." << endl;
}
break;
case 3:
int valorEliminar;
cout << "Elemento a eliminar: ";
cin >> valorEliminar;
if (busqueda(Node::lista, valorEliminar)){
Eliminar(root, valorEliminar);
for(auto it = Node::lista.begin(); it != Node::lista.end(); ++it) {
if (*it == valorEliminar) {
Node::lista.erase(it);
break;
}
}
cout << "Elemento eliminado." << endl;
break;
} else {
cout << valorEliminar << "no existe" << endl;
}
case 4:
break;
default:
cout << "Ingresa un valor valido." << endl;
}
} while (decision != 4);
Node::lista.clear();
cout << "Â¿Deseas realizar otra operaciÃ³n? (1 para sÃ, 0 para no): ";
cin >> decision;
} while (decision == 1);
return 0;
}