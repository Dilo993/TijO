class StudentManagement:
    """
    Klasa zarzadzajaca studentami i ich ocenami.
    """
    def __init__(self):
        self.student_list = []
        self.grade_list = []

    def add_student(self, id: str, name: str, age: int) -> bool:
        """
        Dodaje nowego studenta do bazy danych.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli dodanie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        if age <= 0 or age > 150:
            return False
        else:
            self.student_list.append({'id': id, 'name': name, 'age': age})
            return True

    def update_student(self, id: str, name: str, age: int) -> bool:
        """
        Aktualizuje dane istniejacego studenta na podstawie identyfikatora.

        Args:
            name: Imie studenta.
            age: Wiek studenta.
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli aktualizacja zakonczyla sie sukcesem.
            False w przeciwnym wypadku.
        """
        for student in self.student_list:
            if age <= 0 or age > 150:
                return False
            if student['id'] == id:
                student['name'] = name
                student['age'] = age
                return True
        return False

    def remove_student(self, id: str) -> bool:
        """
        Usuwa studenta z bazy danych na podstawie jego identyfikatora.

        Args:
            id: Unikalny identyfikator studenta.

        Returns:
            True, jesli usuniecie zakonczylo sie sukcesem.
            False w przeciwnym wypadku.
        """
        for student in self.student_list:
            if student['id'] == id:
                self.student_list.remove(student)
                return True
        return False

    def add_grade(self, student_id: str, subject: str, grade: float) -> bool:
        """
        Dodaje ocene z danego przedmiotu dla okreslonego studenta.

        Args:
            student_id: Unikalny identyfikator studenta.
            subject: Nazwa przedmiotu.
            grade: Ocena.

        Returns:
            True, jesli dodanie oceny zakonczylo sie sukcesem (2.0, 3.0, 3.5, 4.0, 4.5, 5.0), 
            False w przeciwnym razie.
        """
        if grade in [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]:
            if not any(student['id'] == student_id for student in self.student_list):
                return False
            self.grade_list.append({'student_id': student_id, 'subject': subject, 'grade': grade})
            return True
        return False

    def avg_grades(self, subject: str) -> float:
        """
        Oblicza srednia ocen z danego przedmiotu dla wszystkich studentow.

        Args:
            subject: Nazwa przedmiotu.

        Returns:
            Srednia ocen z przedmiotu jako liczba zmiennoprzecinkowa.
        """
        total = 0
        count = 0
        for grade in self.grade_list:
            if grade['subject'] == subject:
                total += grade['grade']
                count += 1
        return total / count if count > 0 else 0.0
    