package com.telBot.bot.Repo;

import com.telBot.bot.model.Dish;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;


@Repository
public interface DishRepository extends JpaRepository<Dish,Long> {
    @Query( value = "select d1.id as q,d2.id as qq,d3.id as qqq from dishes d1,dishes d2,dishes d3" +
            " where d1.type='breakfast' and d2.type='dinner' and d3.type='dinner'\n" +
            "and d1.diet=?3 and d2.diet=?3 and d3.diet=?3\n" +
            "and d1.calories + d2.calories + d3.calories < ?1\n" +
            "and d1.calories + d2.calories + d3.calories > ?2 ORDER BY RANDOM() LIMIT 1 ", nativeQuery = true)
    List<Long[]> findRation(double big, double small, String diet);

    @Query( value = "select d1.id as q,d2.id as qq,d3.id as qqq from dishes d1,dishes d2,dishes d3" +
            " where d1.type='breakfast' and d2.type='dinner' and d3.type='dinner'\n" +
            "and d1.calories + d2.calories + d3.calories < ?1\n" +
            "and d1.calories + d2.calories + d3.calories > ?2 ORDER BY RANDOM() LIMIT 1 ", nativeQuery = true)
    List<Long[]> findRationNormal(double big, double small);

}
