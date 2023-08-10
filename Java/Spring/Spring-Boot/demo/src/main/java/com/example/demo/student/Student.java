package com.example.demo.student;

import java.time.LocalDate;

public class Student {
    private Long id;
    private String name;
    private String email;
    private LocalDate birthday;
    private Integer age;

    public Student() {}

    public Student(Long id, String name, String email, LocalDate birthday, Integer age) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.birthday = birthday;
        this.age = age;
    }

    // Dejamos que la base de datos genere el ID por nosotros
    public Student(String name, String email, LocalDate birthday, Integer age) {
        this.name = name;
        this.email = email;
        this.birthday = birthday;
        this.age = age;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public LocalDate getBirthday() {
        return birthday;
    }

    public Integer getAge() {
        return age;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", birthday=" + birthday +
                ", age=" + age +
                '}';
    }
}
