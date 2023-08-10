package com.example.demo.student;

import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import java.beans.BeanProperty;
import java.beans.JavaBean;
import java.time.LocalDate;
import java.time.Month;
import java.util.List;

@Service
public class StudentService {
    public List<Student> getStudent() {
        return List.of(
                new Student(
                    1L,
                    "Marian",
                    "lady@gmail.com",
                    LocalDate.of(2000, Month.FEBRUARY, 24),
                    23
                )
        );
    }
}
