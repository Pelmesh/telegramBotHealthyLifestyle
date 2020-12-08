package com.telBot.bot.api;

import com.telBot.bot.Repo.DishRepository;
import com.telBot.bot.Repo.RationRepository;
import com.telBot.bot.Repo.UserRepository;
import com.telBot.bot.model.Dish;
import com.telBot.bot.model.Ration;
import com.telBot.bot.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/ration")
public class RationApiController {
    @Autowired
    private RationRepository rationRepository;

    @Autowired
    private DishRepository dishRepository;

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public Ration getRation(@RequestParam Long idChat) {
        Ration ration = new Ration();
        User user = userRepository.findByIdChat(idChat);
        List<Long[]> list = new ArrayList<>();
        if (user.getBody().getPurpose() == 0) {
            if (!user.getBody().getTypeDiet().equals("normal")) {
                list = dishRepository.findRation(
                        user.getBody().getCalRate() - 100,
                        user.getBody().getCalRate() - 300,
                        user.getBody().getTypeDiet());
            } else {
                list = dishRepository.findRationNormal(
                        user.getBody().getCalRate() - 100,
                        user.getBody().getCalRate() - 300);
            }
        } else if (user.getBody().getPurpose() == 1) {
            if (!user.getBody().getTypeDiet().equals("normal")) {
                list = dishRepository.findRation(
                        user.getBody().getCalRate() + 300,
                        user.getBody().getCalRate() + 100,
                        user.getBody().getTypeDiet());
            } else {
                list = dishRepository.findRationNormal(
                        user.getBody().getCalRate() + 300,
                        user.getBody().getCalRate() + 100);
            }
        } else if (user.getBody().getPurpose() == 2) {
            if (!user.getBody().getTypeDiet().equals("normal")) {

                list = dishRepository.findRation(
                        user.getBody().getCalRate() + 150,
                        user.getBody().getCalRate() - 150,
                        user.getBody().getTypeDiet());
            } else {
                list = dishRepository.findRationNormal(
                        user.getBody().getCalRate() + 150,
                        user.getBody().getCalRate() - 150);
            }
        }
        List<Long> list2 = list.stream()
                .flatMap(Arrays::stream)
                .collect(Collectors.toList());
        ration.setBreakfast(dishRepository.findById(list2.get(0)).get());
        ration.setDinner(dishRepository.findById(list2.get(1)).get());
        ration.setLunch(dishRepository.findById(list2.get(2)).get());
        java.sql.Date sqlDate = new java.sql.Date(Calendar.getInstance().getTimeInMillis());
        Calendar c = Calendar.getInstance();
        c.setTime(sqlDate);
        c.add(Calendar.DAY_OF_YEAR, 1);
        java.sql.Date sqlDate2 = new java.sql.Date(c.getTimeInMillis());
        ration.setDate(sqlDate2);
        ration.setUser(user);
        ration.setPurpose(user.getBody().getPurpose());
        rationRepository.save(ration);
        return ration;
    }

}
