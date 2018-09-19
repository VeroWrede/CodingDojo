using Microsoft.AspNetCore.Mvc;
using System;

namespace Portfolio1.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]
        public IActionResult Index() 
        {
            Console.WriteLine("in controller");
            return View();
        }
    }
    
}