
#include <iostream>
#include <list>
#include <algorithm>
#include <thread>
#include <chrono>
#include <random>

using namespace std;


int main(){
    
    list<string> students = {
        "Alex", "Anna", "Arda", "Charlotte", "Daniel", 
        "Emily", "Jack", "James", "Liam", "Lucas", 
        "Mert", "Mia", "Oliver", "Sophia", "William"
    };
    int choice;
    string ad_student;
    string student_delete;
    //Values
    
    
    random_device rd;
    mt19937 gen(rd());
    //these lines are needen for chosing students randomly
    
    
    //loop
    do{
        //menu
        cout << "\n Teacher Control Panel \n";
        cout<<endl;
        cout << "--- List of the students ---\n";
        for (const string& student : students) {
            cout << student << endl;
        }
        cout<<"-----------------------------"<<endl;
        cout<<endl;
        cout << "1. Add Student\n";
        cout << "2. Delete a student\n";
        cout << "3. Choose a random student\n";
        cout << "4. Sort all students by their name\n";
        cout << "5. Exit\n";
        cout<<endl;
        cout << "Select an option== ";
        cin >> choice;
        
        //Adds a new student by using function students.push.back
        if (choice==1){
            cout<<"\nEnter the name of the student==";
            cin >> ad_student;
            students.push_back(ad_student);
            cout<< "The new student '"<<ad_student<<"' has been added to the list!";
            this_thread::sleep_for(chrono::seconds(3));
        }
        //Delete students from list by using remove function
        else if (choice==2){
            cout << "\nChoose the student you want to delete =";
            cin >> student_delete;
            if (find(students.begin(), students.end(), student_delete) == students.end()) {
                cout << "\nThere is no student called == "<< student_delete<<endl;
                
                this_thread::sleep_for(chrono::seconds(3));
            } else {
                students.remove(student_delete);
                cout << "\nStudent "<< student_delete << " deleted" <<endl;
                
                this_thread::sleep_for(chrono::seconds(3));
            }
        }
        //most complicated one choosing random students I miss python :(
        else if (choice==3){
            //to check if it is empty
            if (students.empty()){
                cout << "\nThere is no students! add some!"<<endl;
                
            }else {
                cout << "\nChoosing the student";
                for(int i = 0; i < 3; ++i) {
                    cout << ".";
                    cout.flush();
                    //to print every stage of the system 
                    this_thread::sleep_for(chrono::milliseconds(500));
                }
                cout << endl;
                //Chosing a random index
                uniform_int_distribution<int> distrib(0, students.size() - 1);
                int randomIndex = distrib(gen);
                //these lines of code provides us to have acces to a list elements that doesnt have index
                //iterator
                auto it = students.begin();
                advance(it, randomIndex);
                
            cout << "Selected Random Student = " << *it << endl;
            this_thread::sleep_for(chrono::seconds(3));
            }
        }
        else if (choice==4){
            //this is easy one you are just writing a one function and its done
            students.sort();
            cout << "\nStudents have been sorted alphabetically!\n";
            this_thread::sleep_for(chrono::seconds(2));
        }
            
    }while (choice != 5);
    
    cout << "--- List of the students ---\n";
    for (const string& student : students) {
            cout << student << endl;
        }
    cout <<"\nExiting Program";
    return 0;
}