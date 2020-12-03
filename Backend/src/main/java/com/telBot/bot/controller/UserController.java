package com.telBot.bot.controller;

import com.telBot.bot.Repo.BodyRepository;
import com.telBot.bot.Repo.RationRepository;
import com.telBot.bot.model.Body;
import com.telBot.bot.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class UserController {
    @Autowired
    private RationRepository rationRepository;

    @Autowired
    private BodyRepository bodyRepository;

    @GetMapping
    public String getUser(@AuthenticationPrincipal User user, Model model){
        model.addAttribute("user",user);
        model.addAttribute("body",bodyRepository.findByIdChat(user.getIdChat()));
        model.addAttribute("rations",rationRepository.findAllByUser(user));
        return "userInfo";
    }

    @GetMapping("update")
    public String getBody(@AuthenticationPrincipal User user, Model model){
        model.addAttribute("user",user);
        model.addAttribute("body",bodyRepository.findByIdChat(user.getIdChat()));
        return "update";
    }

    @PostMapping("update")
    public String updateBody(@AuthenticationPrincipal User user, Body body,Model model){
        Body bodyU = bodyRepository.findByIdChat(user.getIdChat());
        bodyU.setWeight(body.getWeight());
        bodyU.setAge(body.getAge());
        bodyU.setPurpose(body.getPurpose());
        bodyU.setHeight(body.getHeight());
        model.addAttribute("user",user);
        setAmrBmr(bodyU);
        bodyRepository.saveAndFlush(bodyU);
        return "redirect:/";
    }
    public void setAmrBmr(Body body){
        if(body.getGender().equals("MALE")) {
            body.setBMR(88.4 + (13.4 * body.getWeight()) + (4.8 + body.getHeight()) - (5.7 * body.getAge()));
        }
        if(body.getGender().equals("FEMALE")) {
            body.setBMR(448 + (9.2 * body.getWeight()) + (3.1 + body.getHeight()) - (4.2 * body.getAge()));
        }
        body.setCalRate(body.getBMR() * body.getAMR());
    }
}
