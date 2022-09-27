vector<int> gradingStudents(vector<int> grades) {
 
   int l=grades.size();
   for(int i=0;i<l;i++){
    int multi=(grades[i]/5+1)*5;
    if(grades[i]>=38 && (multi-grades[i])<3 )
        grades [i]=multi;
   }
return grades;
}
